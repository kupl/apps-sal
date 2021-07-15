def main():
    n = int(input())
    a = [int(s) for s in input().split()]
    b = sorted(a)
    am = min(a)
    for i, e in enumerate(a):
        if e % am != 0 and b[i] != e:
            return "NO"
    return "YES"





tests = int(input())
for _ in range(tests):
    print(main())
