n = int(input())
a = input().split()
b = [0]*n
b[0] = int(a[0])
for i in range(1,n):
    b[i] = int(a[i])-int(a[i-1])
works = 0
out = ""
for j in range(1,n+1):
    bo = True
    for k in range(n):
        if b[k] != b[k%j]:
            bo = False
            break
    if bo:
        works += 1
        out += str(j) + " "
print(works)
print(out[:-1])

