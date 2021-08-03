n = int(input())
a = [int(w) for w in input().split()]

s = sum(abs(x) for x in a)
if len(a) == 1:
    print(a[0])
elif all(x > 0 for x in a) or all(x < 0 for x in a):
    print(max(abs(s - 2 * abs(x)) for x in a))
else:
    print(s)
