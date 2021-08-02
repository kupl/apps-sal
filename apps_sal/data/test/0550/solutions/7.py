def normalize_login(login):
    return login \
        .lower() \
        .replace("o", "0") \
        .replace("i", "1") \
        .replace("l", "1")


new_login = normalize_login(input())
n = int(input())
logins = []
for i in range(0, n):
    login = normalize_login(input())
    logins.append(login)

print("No" if new_login in logins else "Yes")
