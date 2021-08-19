n = int(input())
a = [int(x) for x in input().split()]
(mn, mx) = (min(a), max(a))
cnt = 0
for a_i in a:
    if a_i != mn and a_i != mx:
        cnt += 1
print(cnt)
