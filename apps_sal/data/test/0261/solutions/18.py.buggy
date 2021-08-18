import collections


input()
m = collections.defaultdict(set)
for i, ch in enumerate(input()):

    if ch == "*":

        m[i]
        for j in tuple(m):

            if i != j:

                m[min(i, j)].add(max(i, j) - min(i, j))

for node in sorted(m):

    for size in m[node]:

        count = 0
        current_node = node
        while count != 4:

            if size in m[current_node]:

                current_node += size
                count += 1

            else:

                break

        if count == 4:

            print("yes")
            return

print("no")
