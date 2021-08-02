import collections

m, t, r = list(map(int, input().split()))
w = list(map(int, input().split()))

result = 0
current = collections.deque()
used = set()


def main():
    nonlocal result, current
    for ghost in w:
        while current and current[0] < ghost:
            current.popleft()
        required = r - len(current)
        result += required
        moment = ghost
        for i in range(required):
            moment -= 1
            while moment in used:
                moment -= 1
            if ghost - moment > t:
                print(-1)
                return
            used.add(moment)
            current.append(moment + t)
        current = collections.deque(sorted(current))
    print(result)


main()
