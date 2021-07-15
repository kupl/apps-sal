for tc in range(int(input())):
    input()
    lsa = list(map(int, input().split()))
    lsb = list(map(int, input().split()))
    print('YES' if max(max(lsa),max(lsb)) in lsa else 'NO')

