

def main():
    count_of_friends = int(input())
    list_of_friends_chances = [float(i) for i in input().split(' ')]
    list_of_friends_chances.sort()
    max_number = max(list_of_friends_chances)
    list_of_lists = []
    for t in range(0, count_of_friends):
        list_last = []
        for i in range(t, count_of_friends):
            var_temp = list_of_friends_chances[i]
            for j in range(t, count_of_friends):
                if i != j:
                    var_temp *= 1 - list_of_friends_chances[j]
            list_last.append(var_temp)
        list_of_lists.append(sum(list_last))
    max_sum_of_lists = max(list_of_lists)
    if max_sum_of_lists > max_number:
        print(max_sum_of_lists)
    else:
        print(max_number)

def __starting_point():
    main()
__starting_point()
