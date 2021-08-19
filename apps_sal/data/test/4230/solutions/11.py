(X, N) = map(int, input().split())
p = list(map(int, input().split()))
diff = 0
while True:
    num_p = X + diff
    num_m = X - diff
    if num_m not in p:
        print(num_m)
        break
    elif num_p not in p:
        print(num_p)
        break
    else:
        diff += 1
