def remove(s,t,start,end):
    arr = []
    for i in range(start):
        arr.append(s[i])

    for i in range(end+1,len(s)):
        arr.append(s[i])


    i = 0
    j = 0
    while i < len(arr) and j < len(t):
        if arr[i] == t[j]:
            i += 1
            j += 1
        else:
            i += 1

    if j == len(t):
        return True

    return False

def solve(s,t):
    n = len(s)
    ans = 0
    for i in range(n):
        for j in range(i,n):
            if remove(s,t,i,j):
                ans = max(ans,j-i+1)

    print(ans)

def main():
    s = input()
    t = input()
    solve(s,t)


main()

