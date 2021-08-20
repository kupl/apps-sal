def main():
    (N, M) = list(map(int, input().split()))
    if M == N:
        return 'Yes'
    else:
        return 'No'


print(main())
