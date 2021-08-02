n = int(input())
lb = 0
rb = n
while lb != rb:
    mb = (lb + rb + 1) // 2
    if mb * (mb + 1) // 2 < n:
        lb = mb
    else:
        rb = mb - 1
print(n - lb * (lb + 1) // 2)
