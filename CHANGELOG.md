# Changelog
All notable changes to this project will be documented in this file.
This file is following [keep-a-changelog](https://keepachangelog.com).

## [Unreleased](https://github.com/kupl/apps-sal)

### Added
- List utility functions (`map` and `filter`) for processing `Dataset`.
- Implement exporting dataset as `jsonl` format.
- Querying a data element with its id.

### Changed
- Installation method with `https` instead of `ssh`.

## [v0.1.0](https://github.com/kupl/apps-sal/releases/v0.1.0) - 2021-12-10

### Fixed
- Use project logger instead of configuring root logger.

## [v0.0.2](https://github.com/kupl/apps-sal/releases/v0.0.2) - 2021-11-08

### Changed
- Format solutions with `ast` module and `autopep8`.
- Change default Python version to `3.9`.

### Removed
- Remove duplicated solutions.
- Delete comments in solutions.

## [v0.0.1](https://github.com/kupl/apps-sal/releases/v0.0.1) - 2021-08-06

### Added
- The project is created!
- Devcontainer setting.
- Original data is from [here](https://github.com/hendrycks/apps).
- `apps_sal` library that handles the dataset.
