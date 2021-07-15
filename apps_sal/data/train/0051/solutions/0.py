def main():
    t = int(input())
    for z in range(t):
        n, k, d1, d2 = map(int, input().split())
        if n % 3 != 0:
            print('no')
            continue
        f = 0
        for i in [-1, +1]:
            for j in [-1, +1]:
                w = (k - i * d1 - j * d2)
                if f == 0 and (w % 3 == 0) and (n//3)>=(w//3)>=0 and (n//3)>=(w//3 + i * d1)>=0 and (n//3)>=(w//3 + j * d2)>=0:
                    print('yes')
                    f = 1
        if f == 0:
            print('no')
main()
