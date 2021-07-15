import string

def make_link(G, char1, char2):
    if char1 in G:
        if char2 in G[char1]:
            return
        else:
            G[char1].append(char2)
    else:
        G[char1] = [char2]

def make_order(G, str1, str2):
    for i in range(min(len(str1), len(str2))):
        if str1[i] != str2[i]:
            make_link(G, str1[i], str2[i])
            return True

    if len(str2) > len(str1):
        return True
    else:
        return False

def topological_sort(G, ans, k = '', visited = {}):
    if visited.get(k, True) == False:
        return True
    if k not in visited:
        visited[k] = False
        for next in G.get(k, []):
            if topological_sort(G, ans, next, visited):
                return True
        visited[k] = True
        ans.insert(0, k)
    return False

def main():
    N = int(input())

    strs = [input() for i in range(N)]

    G = {}

    for i in range(N-1):
        if not make_order(G, strs[i], strs[i + 1]):
            print("Impossible")
            return

    G[''] = reversed(string.ascii_lowercase)

    ans = []
    if topological_sort(G, ans):
        print("Impossible")
    else:
        print(''.join(ans))

main()
