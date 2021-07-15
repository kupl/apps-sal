def main():
    n, m = list(map(int, input().split()))
    a = [list(map(int, input().split())) for i in range(m)]
    z = min(y - x + 1 for x, y in a)
    print (z)
    print( ' '.join([str(i % z) for i in range(n)]))

main()

