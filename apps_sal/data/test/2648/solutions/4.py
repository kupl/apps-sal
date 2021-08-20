import collections
N = int(input())
AN = list(map(int, input().split()))
an = collections.Counter(AN)
a = sorted(list(an.values()), reverse=True)
al = len(a)
print(al if al % 2 == 1 else al - 1)
