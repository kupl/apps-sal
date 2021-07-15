n = int(input())
li = [int(str(i)*3) for i in range(10)]
import bisect
x = bisect.bisect_left(li,n)
print(li[x])
