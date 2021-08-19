(n, k) = list(map(int, input().split()))
'\na+b = K i\nb+c = K j\nc+a = K k\n2(a+b+c) = K(i+j+k)\n\nk%2=0ならば,\na+b+cはk//2の倍数でなければならない、かつ、差を取ると結局a,b,cがそれぞれk//2の倍数\nでなければならい。それでa+b,b+c,c+dはｋの倍数だから、a,b,cはすべて偶数またはすべて奇数\nでなければならない。\n\nそれ以外の場合、\na+b+cがkの倍数である必要があり、かつ差を取ると結局a,b,cがすべてkの倍数でなければ\nならない。\n'
if k % 2 == 0:
    k //= 2
    a = n // k
    even = a // 2
    if a % 2 == 0:
        odd = even
    else:
        odd = even + 1
    ans = even ** 3 + odd ** 3
else:
    ans = (n // k) ** 3
print(ans)
