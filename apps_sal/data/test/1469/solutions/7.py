
def get_node(num):
    now_num = 1
    count = 1
    while 1:
        if now_num > num:
            count -= 1
            break
        count += 1
        now_num *= 2
    return count

def get_ans_data(node_num):
    ans_data = []
    for i in range(1, node_num):
        data = [i, i + 1, 2**(i - 1)]
        data2 = [i, i + 1, 0]
        ans_data.append(data)
        ans_data.append(data2)
    return ans_data

def main():
    num = int(input())

    node_num = get_node(num)
    ans_data = get_ans_data(node_num)

    now_path = 2 ** (node_num - 1)
    now_num = node_num - 1


    for i in range(now_num, 0, -1):
        now_data = 2 ** (i - 1)
        if num - now_data >= now_path:
            ans_data.append((i, node_num, num - now_data))
            num -= now_data

    print((node_num, len(ans_data)))
    for data in ans_data:
        print((' '.join(list(map(str, data)))))


def __starting_point():
    main()

__starting_point()
