a, b, c = input().split()
len_a = len(a)
len_b = len(b)

if(a[len_a-1] == b[0] and b[len_b-1] == c[0]):
    print("YES")
else:
    print("NO")
