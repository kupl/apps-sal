from collections import defaultdict


def main():
    n, q = list(map(int, input().split()))
    instrs = [input().split() for _ in range(q)]

    instr_dict = defaultdict(list)
    for src, dest in instrs:
        instr_dict[dest].append(src)

    strs = set()
    last_q = set('a')
    for _ in range(n - 1):
        next_q = set()
        for s in last_q:
            rules = instr_dict[s[0]]
            s = s[1:]
            for rule in rules:
                next_q.add(rule + s)
        last_q = next_q

    print(len(last_q))


main()
