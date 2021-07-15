def main():
    n = int(input())

    p = [int(s) for s in input().split()]

    vowels = {'a', 'e', 'i', 'o', 'u', 'y'}

    for i in range(n):
        l = input()
        numv = sum(1 for c in l if c in vowels)
        if numv != p[i]:
            print('NO')
            return
    print('YES')

main()

