import bisect
N = int(input())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())))
C = sorted(list(map(int, input().split())))

ans=0
for b in B:
    a_index = bisect.bisect_left(A, b)
    c_index = bisect.bisect_right(C, b)
    ans += a_index * (N-c_index)
    
print(ans)
