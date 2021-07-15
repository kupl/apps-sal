
def isPossible(a):
    n = len(a)
    for i in range(2,n):
        if a[i] < a[i-1] + a[i-2]:
            return True
    return False



def __starting_point():
    n = int(input().strip())
    a = list(map(int, input().strip().split()))
    a = sorted(a)

    if isPossible(a):
        print("YES")
    else:
        print("NO")


    


__starting_point()
