
line1 = input().split(" ")
n = int(line1[0])
k = int(line1[1])

main = list(map(int, input().split(" ")))

reqs = [None] * (n + 1) # [course_number : [dependency1, dependecy2, ...]]

for i in range(n):
    line = input().split(" ")
    if int(line[0]) == 0:
        reqs[1 + i] = []
    else:
        curr_reqs = []
        for req in line[1:]:
            curr_reqs += [int(req)]
        reqs[1 + i] = curr_reqs

res = []

# print(reqs)
to_exit = False  # чтобы по фасту выходить из циклов

def traverse(main_courses): # сюда передается сразу массив
    nonlocal res,to_exit
    roots =[False] * (n+1)
    while main_courses and not to_exit: # пока мэин не пустой и не нужно ливать из цикла
        main_to_trav = main_courses.pop()
        if reqs[main_to_trav] == None:
            continue
        stack = [main_to_trav] # добавляем корень дерева в стэк
        while len(stack) > 0 and not to_exit:
            to_traverse = stack.pop() # достаем из стэка вершину которую хотим обойти
            if reqs[to_traverse] is not None: # если ее еще не обошли
                childs = reqs[to_traverse]  # берем детей
                if len(childs) == 0: # если детей нет - обходим вершину
                    roots[to_traverse] = False
                    res.append(to_traverse)
                    reqs[to_traverse] = None # помечаем что прошли вершину
                else:
                    roots[to_traverse] = True
                    # print (roots)
                    stack.append(to_traverse) # если дети есть - добавляем сначала себя в стэк(чтобы обойти потом), потом детей

                    for child in childs:
                        if roots[child] == True:
                            print(-1)
                            to_exit = True
                            break

                    stack += childs
                    reqs[to_traverse] = [] # после того как добавили детей - обнуляем их, чтобы больше не добавлять

traverse(main)

if not to_exit:
    print(len(res))
    print(' '.join(map(str, res)))
