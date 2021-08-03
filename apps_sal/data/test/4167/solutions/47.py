n, k = list(map(int, input().split()))

"""
a+b = K i
b+c = K j
c+a = K k
2(a+b+c) = K(i+j+k)

k%2=0ならば,
a+b+cはk//2の倍数でなければならない、かつ、差を取ると結局a,b,cがそれぞれk//2の倍数
でなければならい。それでa+b,b+c,c+dはｋの倍数だから、a,b,cはすべて偶数またはすべて奇数
でなければならない。

それ以外の場合、
a+b+cがkの倍数である必要があり、かつ差を取ると結局a,b,cがすべてkの倍数でなければ
ならない。
"""

if k % 2 == 0:
    k //= 2
    a = n // k
    even = a // 2
    if a % 2 == 0:
        odd = even
    else:
        odd = even + 1
    ans = even**3 + odd**3
else:
    ans = (n // k)**3
print(ans)
