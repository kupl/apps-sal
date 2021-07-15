def main():
    n,k = list(map(int,input().split()))
    ans = 0
    if k%2==0:
        kouho1 = []
        kouho2 = []
        for i in range(1,n+1):
            if i%k==0:
                kouho1.append(i)
            elif i%k == k/2:
                kouho2.append(i)
        ans += len(kouho1)**3
        ans+= len(kouho2)**3
    else:
        kouho = []
        for i in range(1,n+1):
            if i%k==0:
                kouho.append(i)
        ans += len(kouho)**3

    print(ans)
main()

