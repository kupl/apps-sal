def main():
    n,s = input().split()
    n = int(n)
    ans = 0
    for i in range(n):
        at=gc=0
        for si in s[i:]:
            if si=="A":
                at += 1
            elif si=="T":
                at -= 1
            elif si=="C":
                gc -= 1
            else:
                gc += 1
            if at==0 and gc==0:
                ans += 1
    print(ans)

main()
