([c, d], [n, m], k) = (list(map(int, input().split())),
                       list(map(int, input().split())), int(input()))
left = n * m - k
if left <= 0:
    print(0)
else:
    print(min(left // n * c + left % n * d, (left + n - 1) // n * c, left * d))
