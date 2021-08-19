(N, K, Q) = map(int, input().split())
alist = list(map(int, input().split()))


def div_by_a(border, dlist):
    divided_list = []
    div = []
    for d in dlist:
        if d < border:
            if len(div) > 0:
                div.sort()
                divided_list.append(div)
                div = []
        else:
            div.append(d)
    else:
        if len(div) > 0:
            div.sort()
            divided_list.append(div)
    return divided_list


answer = 10 ** 9
for a in alist:
    divlist = div_by_a(a, alist)
    cand_list = []
    for div in divlist:
        cand_num = max(0, len(div) - K + 1)
        cand_list.extend(div[:cand_num])
    cand_list.sort()
    if len(cand_list) >= Q:
        answer = min(answer, cand_list[Q - 1] - a)
print(answer)
