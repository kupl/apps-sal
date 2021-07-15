# coding: utf-8
# Your code here!
import sys
readline = sys.stdin.readline
read = sys.stdin.read

n, = map(int,readline().split())
*a, = map(int,readline().split())
*b, = map(int,readline().split())
b = b[::-1]

same = [i for i in range(n) if a[i] == b[i]]
if same:
    v = a[same[0]] # b を逆順にしたので、重なる値は一種類しかない。これを v とおく。
    notv = [i for i in range(n) if a[i]!=v and b[i]!=v] # どっちもvとかぶらない index
    if len(same) > len(notv):
        print("No")
        return
    for i,j in zip(same,notv):
        b[i],b[j] = b[j],b[i]

print("Yes")
print(*b)
