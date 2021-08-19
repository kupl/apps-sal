import math


def main():
    s = str(input())
    t = str(input())
    st_dict = dict()
    for i in range(len(t)):
        if s[i] != t[i]:
            if s[i] in list(st_dict.keys()) and st_dict[s[i]] != t[i]:
                print(-1)
                return
            st_dict[s[i]] = t[i]
            st_dict[t[i]] = s[i]
    result = ''
    for i in range(len(t)):
        if t[i] in list(st_dict.keys()):
            result += st_dict[t[i]]
        else:
            result += t[i]
    if result == s:
        print(int(len(list(st_dict.keys())) / 2))
        for key in list(st_dict.keys()):
            if key > st_dict[key]:
                print('{} {}'.format(key, st_dict[key]))
    else:
        print(-1)


main()
