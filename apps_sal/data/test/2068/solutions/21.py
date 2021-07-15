n = int(input())
reposted_list = {"polycarp": 1}

for i in range(n):
    reposter, r, author = input().split(" ")
    reposter, author = reposter.lower(), author.lower()
    reposted_list[reposter] = reposted_list[author] + 1

print(reposted_list[max(reposted_list, key=reposted_list.get)])
