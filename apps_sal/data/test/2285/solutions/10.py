n = int(input())
list = []
for i in range(n):
    str = input()
    list = str.split(":")
    if(str.count("::") > 0):
        t = list.count("")
        if(t == 3):
            t = "0000:" * 8
            print(t[:len(t) - 1])
        elif t == 2:
            if str[0:2] == '::':

                str = str.replace("::", "0000:" * (10 - len(list)))
                res = ""
                list2 = str.split(":")
                for i in range(len(list2)):
                    res += '0' * (4 - len(list2[i])) + list2[i] + ":"
                print(res[0:len(res) - 1])

            else:
                str = str.replace("::", ":0000" * (10 - len(list)))
                res = ""
                list2 = str.split(":")
                for i in range(len(list2)):
                    res += '0' * (4 - len(list2[i])) + list2[i] + ":"
                print(res[0:len(res) - 1])
        else:
            str = str.replace("::", ":0000:" * (9 - len(list)))
            str = str.replace("::", ":")
            res = ""
            list2 = str.split(":")
            for i in range(len(list2)):
                res += '0' * (4 - len(list2[i])) + list2[i] + ":"
            print(res[0:len(res) - 1])

    else:
        res = ""
        for i in range(len(list)):
            res += '0' * (4 - len(list[i])) + list[i] + ":"
        print(res[0:len(res) - 1])
