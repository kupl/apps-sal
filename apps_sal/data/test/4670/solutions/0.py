import re


def my_func(s):
    s = s.upper()
    res = re.search(r'^M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$', s)
    if(s == "MMMM"):
        print("False")
    else:
        if res:
            print("True")
        else:
            print("False")


my_func(input())
