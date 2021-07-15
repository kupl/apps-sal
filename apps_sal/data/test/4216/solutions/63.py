n = int(input())
def solve(n):
    i = 1
    ans = 10000000
    while i*i <= n:
        if n % i == 0:
            lower = i
            if i != n // i:
                upper = n//i
            else:
                upper = i
            anstmp = max(len(str(lower)), len(str(upper)))
            if ans > anstmp:
                ans = anstmp
        i += 1
        
    return ans

print(solve(n))
