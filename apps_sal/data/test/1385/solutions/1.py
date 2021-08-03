def printtag(s):
    print("<" + s + ">")


s = input()
l = s.split("\"")
non_modify = 0
for s in l:
    if non_modify:
        printtag(s)
    else:
        tmp_lst = s.split(" ")
        for st in tmp_lst:
            if len(st):
                printtag(st)
    non_modify = 1 - non_modify
