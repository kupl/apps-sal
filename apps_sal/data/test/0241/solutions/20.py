n, m, v1, v2 = list(map(int, input().split()))
t = list(map(int, input().split()))
t1, t2 = min(t), max(t)
if t1 < v1 or t2 > v2:
    print('Incorrect')
elif (v1 < t1) + (v2 > t2) > n - m:
    print('Incorrect')
else:
    print('Correct')
