def abc067b_snake_toy():
    n, k = map(int, input().split())
    l = sorted(list(map(int, input().split())), reverse=True)
    print(sum(l[0:k]))

abc067b_snake_toy()
