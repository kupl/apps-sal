def main():
    read = lambda: map(int, input().split())
    
    n = int(input())
    a = list(read())
    used = [True] * (n + 1)
    C = {i + 1 for i in range(n)}    
    A = {i for i in a if i <= n}
    B = A ^ C
    for i in a:
        if i > n or not used[i]:
            print(B.pop(), end = ' ')
        else:
            print(i, end = ' ')
            used[i] = False
main()
