def main():
    s = input()
    K = int(input())
    r = set()
    for i in range(97, 97 + 26):
        for j, v in enumerate(s):
            if v == chr(i):
                for k in range(5):
                    r.add(s[j:j + k + 1])
        if len(r) > 5:
            break
    l = list(r)
    l.sort()
    return l[K - 1]


print((main()))
