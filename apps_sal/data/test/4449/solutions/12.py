q = int(input())
for _ in range(q):
    n = int(input())
    a = list(map(int, input().split()))

    def solve(a):
        from collections import Counter
        c = Counter(a)
        keys = sorted(c)
        for key in keys:
            if c[key] % 2 != 0:
                return False
        temp = [[k]*c[k] for k  in keys]
        keys = []
        for t in temp:
            keys += t
        area = keys[0] * keys[-1]
        head = 0
        tail = len(keys) - 1
        if len(keys) % 2 != 0:
            return False
        while head < tail:
            if keys[head] * keys[tail] != area:
                return False
            head += 1
            tail -= 1
        return True
    print("YES" if solve(a) else "NO")

