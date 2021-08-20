def main():
    (n, k) = list(map(int, input().split()))
    candy = list(map(int, input().split()))
    candies = []
    zeroes = 0
    for i in candy:
        mod = i % k
        if mod == 0:
            zeroes += 1
        else:
            candies.append(mod)
    candies.sort()
    boxes = zeroes // 2
    candy_dict = {}
    for i in candies:
        if i not in list(candy_dict.keys()):
            candy_dict[i] = 1
        else:
            candy_dict[i] += 1
    for i in candy_dict:
        if candy_dict[i] > 0:
            if k - i in list(candy_dict.keys()):
                if candy_dict[k - i] > 0:
                    if i == k - i:
                        box = candy_dict[i] // 2
                        candy_dict[i] = candy_dict[i] % 2
                    else:
                        box = min(candy_dict[i], candy_dict[k - i])
                        candy_dict[i] -= box
                        candy_dict[k - i] -= box
                    boxes += box
    print(2 * boxes)


main()
