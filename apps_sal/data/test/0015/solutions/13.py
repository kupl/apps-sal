a, b, c = list(map(int, input().split()))

if((c == 0 and a == b) or (c > 0 and a % c == b % c and b >= a) or (c < 0 and
                                                                    a % c == b % c and b <= a)):
    print("YES")
else:
    print("NO")
