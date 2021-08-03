def main():
    s = input()

    if s.count('[') == 0 or s.count(']') == 0:
        print(-1)
        return

    t = s[s.find('['):s.rfind(']') + 1]

    if t.count(':') < 2:
        print(-1)
        return

    t = t[t.find(':'):t.rfind(':') + 1]
    print(4 + t.count('|'))


main()
