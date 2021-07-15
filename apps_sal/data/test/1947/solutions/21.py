(n, m, length_) = [int(s) for s in input().split(" ")]

a = [int(s) for s in input().split(" ")]

result = 0
prev = None
for i in range(n):
    if prev and prev <= (length_):
        if a[i] > length_:
            result+=1
    if not prev and a[i] > length_:
        result+=1

    prev = a[i]


for i in range(m):
    temp = input()
    if temp == "0":
        print(result)
    else:
        (_, p, d) = [int(s) for s in temp.split(" ")]
        num = p - 1
        cm = d
        old_val = a[num]
        a[num] += cm
        if old_val > length_:
            continue
        if a[num] <= length_:
            continue

        if num!=0 and num!=(n-1):
            if a[num-1] > length_ and a[num+1] > length_:
                result-=1
            elif a[num-1] <= length_ and a[num+1] <= length_:
                result += 1
        elif num == 0 and (len(a)==1 or a[1] <= length_):
            result+=1
        elif num == (n-1) and a[n-2] <= length_:
            result+=1




# easy = True
# for el in a:
#     if el <= length_:
#         easy = False
#
# t = [0]*4*n
#
# def build (a, v, tl, tr):
#     if tl == tr:
#         t[v] = 1 if a[tl] > length_ else 0
#     else:
#         tm = (tl + tr) // 2
#         build (a, v*2, tl, tm)
#         build (a, v*2+1, tm+1, tr)
#         if a[tm] > length_ and a[tm + 1] > length_:
#             t[v] = t[v * 2] + t[v * 2 + 1] -1
#         else:
#             t[v] = t[v * 2] + t[v * 2 + 1]
#
#
#
#
# def update (v, tl, tr, pos):
#     if (tl == tr):
#         if tl == pos:
#             # print(v, tl, pos)
#             t[v] = 1
#     else:
#         tm = (tl + tr) // 2
#         if (pos <= tm):
#             update(v*2, tl, tm, pos)
#         else:
#             update(v*2+1, tm+1, tr, pos)
#         if a[tm] > length_ and a[tm + 1] > length_:
#             t[v] = t[v * 2] + t[v * 2 + 1] - 1
#         else:
#             t[v] = t[v * 2] + t[v * 2 + 1]
#
# if not easy:
#     build(a,1,0,n-1)
# # print(t)
#
# # def evaluate(v, tl, tr, l, r):
# #     if (l > r):
# #         return 0
# #     if (l == tl and r == tr):
# #         return 1 if t[v] > length_ else 0
# #         tm = (tl + tr) // 2
# #     left_result =  evaluate(v*2, tl, tm, l, min(r,tm))
# #     right_result = evaluate(v*2+1, tm+1, tr, max(l,tm+1), r)
# #     if t[tm] > length_ and t[tm+1] > length_:
# #         return left_result + right_result -1
# #     else:
# #         return left_result + right_result
#
# for i in range(m):
#     temp = input()
#     if temp == "0":
#         if easy:
#             print(1)
#         else:
#             print(t[1])
#     else:
#         if easy:
#             continue
#
#         (_, p, d) = [int(s) for s in temp.split(" ")]
#         # print("sss", p, d)
#         num = p - 1
#         cm = d
#         old_val = a[num]
#         a[num] += cm
#         if old_val > length_:
#             continue
#         if a[num] <= length_:
#             continue
#         update(1, 0, n - 1, num)

