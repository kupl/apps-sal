def main():
    N = int(input())
    users = {}
    users['polycarp'] = 1
    for x in range(N):
        msg = input().split()
        (user1, user2) = (msg[0].lower(), msg[2].lower())
        users[user1] = users[user2] + 1
    print(max(users.values()))


main()
