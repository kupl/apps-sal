n = int(input())

parties = list(map(int, input().split()))

acceptable_parties = [(i + 2, p) for i, p in enumerate(parties[1:]) if p * 2 <= parties[0]]

if (parties[0] + sum([p[1] for p in acceptable_parties])) * 2 > sum(parties):
    print(len(acceptable_parties) + 1)
    print(*([1] + [p[0] for p in acceptable_parties]))
else:
    print(0)
