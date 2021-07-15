def solve(arr,n,x,ans):
    arr.sort()
    teams = 0
    size = 0
    while arr:
        min_val = arr.pop()
        size += 1
        if min_val*size >= x:
            teams += 1
            size = 0

    ans.append(teams)

def main():
    t = int(input())
    ans = []
    for i in range(t):
        n,x = list(map(int,input().split()))
        arr = list(map(int,input().split()))
        solve(arr,n,x,ans)

    for i in ans:
        print(i)


main()

