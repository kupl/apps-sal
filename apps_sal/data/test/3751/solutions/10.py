import sys
3
# Copyright (C) 2017 Sayutin Dmitry.
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; version 3
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; If not, see <http://www.gnu.org/licenses/>.


def main():
    has = [False] * 26
    first = [-1] * 26
    cnt = 0
    s = input().strip()

    for i in range(len(s)):
        num = ord(s[i]) - ord('a')
        if not has[num]:
            has[num] = True
            first[num] = i
            cnt += 1

    for i in range(cnt):
        if not has[i]:
            print("NO")
            return

    for i in range(cnt, 26):
        if has[i]:
            print("NO")
            return

    for i in range(1, cnt):
        if first[i - 1] > first[i]:
            print("NO")
            return

    print("YES")


main()
