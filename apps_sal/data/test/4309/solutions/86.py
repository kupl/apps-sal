n = int(input())
hyaku = (n - n % 100) / 100
if n % 100 > hyaku * 10 + hyaku:
    hyaku += 1
    print(int(hyaku * 100 + hyaku * 10 + hyaku))
else:
    print(int(hyaku * 100 + hyaku * 10 + hyaku))
