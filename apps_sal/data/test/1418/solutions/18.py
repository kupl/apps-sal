def solve(n):
    array = [0]*(n+1)
    curr = 1
    for i in range(2,n+1):
        if array[i] == 0:
            j = 1
            while i*j <= n:
                array[i*j] = curr
                j += 1
            curr += 1

    for i in range(2,n+1):
        print(array[i],end = ' ')

def main():
    n = int(input())
    solve(n)

main()

