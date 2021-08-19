# 全探索

n = int(input())


class People:
    def __init__(self):
        self.type = None


peoples = [People() for i in range(n + 1)]


def change_10to2(i):
    ans = format(i, '#0' + str(n + 3) + 'b')[2:]
    return ans


def set_people_type(binary_list, peoples):
    for i, people in enumerate(peoples):
        if i != 0:
            people.type = binary_list[i]


def get_statement():
    shougen = {}
    for i in range(1, n + 1):
        ai = int(input())
        ans = []
        for j in range(ai):
            kumi = [int(k) for k in input().split()]
            ans.append(kumi)
        shougen[str(i)] = ans
    return shougen


shougens = get_statement()


def shougen_dicide(peoples, shougens):
    for i in range(1, n + 1):
        shougen = shougens[str(i)]
        for shou in shougen:
            people, type = shou
            people = int(people)
            type = str(type)
            # 正直者のとき
            if peoples[i].type == "1":
                if peoples[people].type != type:
                    return False

            # #嘘つきのとき
            # else:
            #     if peoples[people].type==type:
            #         return False
    return True


ans = 0
for i in range(2**n):
    binary_list = change_10to2(i)
    set_people_type(binary_list, peoples)
    if shougen_dicide(peoples, shougens):
        ans = max(ans, binary_list.count("1"))
print(ans)
